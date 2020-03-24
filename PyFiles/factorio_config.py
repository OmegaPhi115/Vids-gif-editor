from data.imports_update import *


class config_handler():
    def create(self, name, path):
        path = Path(path)
        new_config = {
            "name": name,
            "path": str(path),
            "exe_path": str(Path.joinpath(path, "bin\\x64\\factorio.exe")),
            "version": get_factorio_version(path)
        }
        factorio_configs.loaded_file["configs"].append(new_config.copy())  # We copy the dict for prevent linked variable mess ups
        factorio_configs.write()
