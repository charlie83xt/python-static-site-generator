from ssg.site import Site, parsers
import typer

def main(source= "content", dest= "dist"):
    config = {
        "source": source,
        "dest": dest,
        parsers: [parsers.ResourceParsers()]
    }

    site = Site(**config).build()

typer.run(main)