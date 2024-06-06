from typing import Any
from definitions import ROOT_PATH
from codec.saves.JSONSavable import JSONSavable
from codec.saves.SaveCodec import SaveCodec

import json
import os


class JSONSaveCodec(SaveCodec[dict[str, Any]]):
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
        self.__saveables: list[JSONSavable] = []

    def register_saveable(self, saveable: JSONSavable) -> None:
        """Register a saveable that can load and receive a json like dictionary.

        Args:
            saveable: The saveable to register
        """
        self.__saveables.append(saveable)

    def load(self) -> dict[str, Any]:
        """Load the data in the JSON save file as a python dictionary.

        Returns:
            The dictionary parsed from the JSON save file

        Raises:
            Exception if the file could not be parsed as a JSON.
        """
        json_load_path: str = f"{ROOT_PATH}/{self._save_path}/{self.SAVE_FILE_NAME}.json"
        with open(json_load_path, "r") as fp:
            try:
                loaded_dict: dict[str, Any] = json.load(fp)
                return loaded_dict
            except Exception as e:
                raise Exception(f"The json save file at: {json_load_path} cannot be parsed as JSON. Error: {e}")
            finally:
                fp.close()

    def save(self) -> None:
        """Notify all registered saveables of a save occuring, and pass in a json like dictionary that saveables
        can use to modify what will be written. Finally, save to the configured save path, whilst creating any
        directories that don't exist.

        Raises:
            Exception when the final state of the json like dictionary cannot be encoded
        """
        save_directory_path: str = f"{ROOT_PATH}/{self._save_path}"

        # notify saveables to save
        for saveable in self.__saveables:
            saveable.on_save(self.__json_dict)

        # if save directory doesn't exist, create the directory
        if not os.path.exists(save_directory_path):
            os.makedirs(save_directory_path)

        # encode json dict as JSON and save as file to path
        with open(f"{save_directory_path}/{self.SAVE_FILE_NAME}.json", "w") as fp:
            try:
                json.dump(self.__json_dict, fp, indent=4)
            except Exception as e:
                raise Exception(f"The final state of the json like dictionary cannot be encoded as json. Error: {e}")
            finally:
                fp.close()
