import json
from pathlib import Path

import click

from src.get_history import GitRepo


@click.command("get-history")
@click.option(
    "--output",
    type=click.Path(dir_okay=True, file_okay=False),
    help="Path to the directory in which to write all the target files' committed versions.",
)
@click.option(
    "--repo",
    type=click.Path(exists=True),
    help="Path to the root of the targeted git repository.",
)
@click.option(
    "--relative-file-name",
    type=click.Path(),
    multiple=True,
    help="Target file's path relative to the git repository.",
)
def cli(output, repo, relative_file_name):
    git_repo = GitRepo(repo)
    outdir = Path(output)
    outdir.mkdir(exist_ok=True, parents=True)
    for output_stem, data in git_repo.retrieve_files(relative_file_name):
        outfile = outdir.joinpath(output_stem)
        if outfile.suffix == ".json":
            with open(outfile, "w") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    cli()
