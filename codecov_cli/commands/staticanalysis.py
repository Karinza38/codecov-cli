import asyncio
import pathlib

import click

from codecov_cli.fallbacks import CodecovOption, FallbackFieldEnum
from codecov_cli.services.staticanalysis import run_analysis_entrypoint


@click.command()
@click.option(
    "--foldertosearch",
    default=".",
    help="Folder to search",
    type=click.Path(path_type=pathlib.Path),
)
@click.option(
    "--numberprocesses", type=click.INT, default=None, help="number of processes to use"
)
@click.option("--pattern", default="*", help="file pattern to search for")
@click.option("--force/--no-force", default=False)
@click.option(
    "--commit-sha",
    "commit",
    help="Commit SHA (with 40 chars)",
    cls=CodecovOption,
    fallback_field=FallbackFieldEnum.commit_sha,
    required=True,
)
@click.option("--token")
@click.pass_context
def static_analysis(
    ctx, foldertosearch, numberprocesses, pattern, commit, token, force
):
    return asyncio.run(
        run_analysis_entrypoint(
            ctx.obj["codecov_yaml"],
            foldertosearch,
            numberprocesses,
            pattern,
            commit,
            token,
            force,
        )
    )
