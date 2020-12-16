from pathlib import Path

from clld.web.assets import environment

import papuanvoices


environment.append_path(
    Path(papuanvoices.__file__).parent.joinpath('static').as_posix(),
    url='/papuanvoices:static/')
environment.load_path = list(reversed(environment.load_path))
