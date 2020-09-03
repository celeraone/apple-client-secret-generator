# Sign In with Apple Client Secret Generator

Script to generate client secret for Sign In with Apple.

## Dependencies

Script depends on `cryptography`, `pyjwt` and `click` libraries. Install them with:

```
pip install cryptography pyjwt click
```

## Usage

In order to generate the secret, following arguments need to be passed to the script:

- `key_file` (the p8 file with private key downloaded from Apple),
- `key_id` (found under your key details in `Keys` tab in Apple Developer Account)
- `team_id` (found on the `Membership` page in Apple Developer Account)
- `client_id` (the `Service ID` registered in Apple Developer Account)
- `validity_period` (in days, maximum value is 180).

Run the script using following command:

```
python create_apple_client_secret.py
    --key_file=<path_to_your_key_file>
    --key_id=<key_id>
    --team_id=<team_id>
    --client_id=<client_id>
    --validity_period=<validity_period>
```

You can also run the script without arguments and you will be
prompted interactively for them.
