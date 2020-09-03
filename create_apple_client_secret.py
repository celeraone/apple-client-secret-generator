# -*- coding: utf-8 -*-
# (c) 2020 CeleraOne GmbH

"""Script to generate Client Secret for Sign In With Apple.

Official documentation can be found in section `Creating the Client Secret` at:
https://developer.apple.com/documentation/sign_in_with_apple/generate_and_validate_tokens

Script usage:

    python create_apple_client_secret.py
        --key_file=<path_to_your_key_file>
        --key_id=<key_id>
        --team_id=<team_id>
        --client_id=<client_id>
        --validity_period=<validity_period>

You can also omit all the options when running the script and you will be
prompted interactively for them.

The output of the script is a JWT, which can be used as `client_secret` in
requests to https://appleid.apple.com/auth/token endpoint.

IMPORTANT: NEVER EXPOSE THE CLIENT SECRET PUBLICLY! IT CAN COMPROMISE SECURITY
OF THE WHOLE APPLICATION IF IT ENDS UP IN THE WRONG HANDS!
"""

import time

import click
import jwt


@click.command()
@click.option('--key_file', prompt='Key file path')
@click.option('--key_id', prompt='Key ID')
@click.option('--team_id', prompt='Team ID')
@click.option('--client_id', prompt='Client ID (Service ID)')
@click.option('--validity_period', prompt='Validity period', default=180)
def main(key_file, key_id, team_id, client_id, validity_period):
    with open(key_file, 'r') as f:
        private_key = f.read()
    payload = {
        'iss': team_id,
        'sub': client_id,
        'iat': int(time.time()),
        'exp': int(time.time()) + 86400 * validity_period,
        'aud': 'https://appleid.apple.com',
    }
    token = jwt.encode(payload, private_key, 'ES256', headers={'kid': key_id})
    click.echo('\nYour Apple Client Secret (NEVER EXPOSE IT PUBLICLY):\n')
    click.echo(token)


if __name__ == '__main__':
    main()
