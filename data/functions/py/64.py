def run(ctx, commandline):
    """Run command with environment variables present."""
    file = ctx.obj['FILE']
    dotenv_as_dict = dotenv_values(file)
    if not commandline:
        click.echo('No command given.')
        exit(1)
    ret = run_command(commandline, dotenv_as_dict)
    exit(ret)