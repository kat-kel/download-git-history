# `gethist` Get historical iterations of a file

This CLI tool saves in a directory all versions of a file that were committed to a git repository.

_Note: Current version only works for JSON files._

To install, create a virtual Python environment with version 3.11, activate it, and run the following `pip install`:

```console
$ pip install git+https://github.com/kat-kel/download-git-history.git
```

# Save versions committed to Git repository

Use the command `gethist` to iterate through all versions of a file committed to a git repository and save them inside a folder. Each version is written to a file whose name is composed of (a) the date of the commit, (b) timestamp of the commit, and (c) the commit's ID.

```console
Usage: gethist [OPTIONS]

Options:
  --output DIRECTORY         Path to the directory in which to write all the
                             target files' committed versions.
  --repo PATH                Path to the root of the targeted git repository.
  --relative-file-name PATH  Target file's path relative to the git
                             repository.
  --help                     Show this message and exit.
```

## Example

Let's say you want to save the committed versions of a file, such as a JSON file that's daily rewritten with updated information, `enriched-urls.json`. The versions were committed in a git repository outside your current working directory (CWD). See the example architecture below.

```console
.
|___git-repo/
    |___main.py
    |___data/
        |___enriched-urls.jon
|___compile-history/ (CWD)
    |___committed-data/
```

To save all the committed versions of `enriched-urls.json` in this example scenario, assign the following information to the `gethist` command's options:

- `--output` : `./versions`
- `--repo` : `../git-repo`
- `--relative-file-name` : `data/enriched-urls.json`

```console
$ gethist --output ./versions --repo ../git-repo --relative-file-name data/enriched-urls.json
```

```console
.
|___git-repo/
    |___main.py
    |___data/
        |___enriched-urls.jon
|___compile-history/ (CWD)
    |___committed-data/
        |___2023-10-23_1698060560.0_723cf1cc67abc66aec6e944db33fbd4909d8bc9a.json
        |___2023-10-23_1698061018.0_666f03899cc7cdd9cb63573df2642f6a2ec3dc68.json
        |___2023-10-24_1698117091.0_76de23c221b08d1ff2945a07a6528e2722ca30c4.json
        |___2023-10-25_1698203473.0_a308fe7493cd843d5da7150f2f3c630f1bc34571.json
        |___2023-10-26_1698289893.0_27ba55bff8a2096465bedec31ce3e0bb188ab4ac.json
```
