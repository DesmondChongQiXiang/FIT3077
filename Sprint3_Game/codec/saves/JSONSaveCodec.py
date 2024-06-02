from typing import Any
from definitions import ROOT_PATH
from codec.saves.JSONSaveable import JSONSaveable
from codec.saves.SaveCodec import SaveCodec

import json


class JSONSaveCodec(SaveCodec):
    """Save to and load from a JSON file using json like python dictionaries.

    Author: Shen
    """

    SAVE_FILE_NAME = "save"  # the file name for the save file

    def __init__(self, save_path: str):
        """Constructor.

        Args:
            save_path: The directory path relative to the root of the project to save the json file to.
        """
        super().__init__(save_path)
        self.__json_dict: dict[str, Any] = dict()
        self.__saveables: list[JSONSaveable] = []

    def register_saveable(self, saveable: JSONSaveable) -> None:
        """Register a saveable that can load and receive a json like dictionary.

        Args:
            saveable: The saveable to register
        """
        self.__saveables.append(saveable)

    def load(self) -> None:
        """Notify all registered saveables of a load occuring, and pass in the data that those saveables can
        use to load themselves.
        """
        for saveable in self.__saveables:
            saveable.on_load(self.__json_dict)

    def save(self) -> None:
        """Notify all registered saveables of a save occuring, and pass in a json like dictionary that saveables
        can use to modify what will be written. Finally, save to the configured save path.

        Raises:
            Exception when the final state of the json like dictionary cannot be encoded
        """
        for saveable in self.__saveables:
            saveable.on_save(self.__json_dict)

        # encode json dict as JSON and save as file to path
        with open(f"{ROOT_PATH}/{self._save_path}/{self.SAVE_FILE_NAME}.json" ,"w") as fp:
            try:
                json.dump(self.__json_dict, fp, indent=4)
            except Exception as e:
                raise Exception(f"The final state of the json like dictionary cannot be encoded as json. Error: {e}")
            finally:
                fp.close()
