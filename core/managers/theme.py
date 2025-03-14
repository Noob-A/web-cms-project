from core.managers.editables import EditableManagers
from core.managers.logging import Log


class ThemeManager():

    style_static = []
    script_static = []

    url_script = []
    url_style = []

    __editables = EditableManagers()

    def __init__(self, call=None) -> None:

        if call == None:
            self.style_static = []
            self.url_style = []
            self.url_script = []
            self.script_static = []

        self.on_load()

    def on_load(self):
        pass

    def get_static(self):
        response = {
            "style": self.style_static,
            "script": self.script_static,
            "url_style": self.url_style,
            "url_script": self.url_script
        }
        # print(response)

        return response

    def load_static(self, static):
        """
        Sets multiple data to static

        arguments:
            static - `array`
        """
        # Definitions

        #
        if "css" in static:
            for st in static["css"]:
                self.load_css(src=st)

        if "js" in static:
            for st in static["js"]:
                self.load_script(src=st)

        if "cdn_css" in static:
            for st in static["cdn_css"]:
                self.load_css(url=st)

        if "cdn_js" in static:
            for st in static["cdn_js"]:
                self.load_script(url=st)

    def define_editable(self, name: str, value, index: int):
        """
        Defines content editable which stores in database
        -

        args:
            `name: str` - Unique name of editable
            `value: any` - Content of editable
            `index: int` - index of editables type 

        available indexes:
            - `0` - text
            - `1` - list
            - `2` - dictionary
        """
        self.__editables.set_editable(name, value, index)
        Log("Method called successfully", 0)

    def load_css(self, src: str = None, url: str = None):
        """
        Sets css data to static
        -

        args:
            `src: str` - source file, set None if using url
            `url: str` - url link to css. Use for CDN, None if using src
        """
        if url:
            exec = self.url_style.append(url)
            return exec

        if not src:
            raise

        self.style_static.append(src)
        Log(f"{src} loaded successfuly", 0)

    def load_script(self, src: str, url: str = None):
        """
        Sets js data to static
        -

        args:
            `src: str` - source file, set None if using url
            `url: str` - CDN url link to js. Use for CDN, None if using src
        """
        if url:
            exec = self.url_script.append(url)
            return exec

        if not src:
            raise

        exec = self.script_static.append(src)
        return exec
