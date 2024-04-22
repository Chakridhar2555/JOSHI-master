import typing as t

from _typeshed import Incomplete
from flask import Flask

from .config import Config
from .extension.library import ElementLibrary
from .page import Page
from .partial import Partial

class _DoNotUpdate: ...

class Gui:
    on_action: Incomplete
    on_change: Incomplete
    on_init: Incomplete
    on_navigate: Incomplete
    on_exception: Incomplete
    on_status: Incomplete
    on_user_content: Incomplete
    def __init__(
        self,
        page: str | Page | None = None,
        pages: dict | None = None,
        css_file: str | None = None,
        path_mapping: dict | None = None,
        env_filename: str | None = None,
        libraries: t.List[ElementLibrary] | None = None,
        flask: Flask | None = None,
    ) -> None: ...
    @staticmethod
    def add_library(library: ElementLibrary) -> None: ...
    @staticmethod
    def register_content_provider(
        content_type: type, content_provider: t.Callable[..., str]
    ) -> None: ...
    @staticmethod
    def add_shared_variable(*names: str) -> None: ...
    @staticmethod
    def add_shared_variables(*names: str) -> None: ...
    def __enter__(self): ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: types.TracebackType | None,
    ): ...
    def add_page(self, name: str, page: str | Page, style: str | None = "") -> None: ...
    def add_pages(
        self, pages: t.Mapping[str, str | Page] | str | None = None
    ) -> None: ...
    def add_partial(self, page: str | Page) -> Partial: ...
    def load_config(self, config: Config) -> None: ...
    def get_flask_app(self) -> Flask: ...
    state: Incomplete
    def run(
        self,
        allow_unsafe_werkzeug: bool = ...,
        async_mode: str = ...,
        change_delay: t.Optional[int] = ...,
        chart_dark_template: t.Optional[t.Dict[str, t.Any]] = ...,
        base_url: t.Optional[str] = ...,
        dark_mode: bool = ...,
        dark_theme: t.Optional[t.Dict[str, t.Any]] = ...,
        data_url_max_size: t.Optional[int] = ...,
        debug: bool = ...,
        extended_status: bool = ...,
        favicon: t.Optional[str] = ...,
        flask_log: bool = ...,
        host: str = ...,
        light_theme: t.Optional[t.Dict[str, t.Any]] = ...,
        margin: t.Optional[str] = ...,
        ngrok_token: str = ...,
        notebook_proxy: bool = ...,
        notification_duration: int = ...,
        propagate: bool = ...,
        run_browser: bool = ...,
        run_in_thread: bool = ...,
        run_server: bool = ...,
        server_config: t.Optional[ServerConfig] = ...,
        single_client: bool = ...,
        system_notification: bool = ...,
        theme: t.Optional[t.Dict[str, t.Any]] = ...,
        time_zone: t.Optional[str] = ...,
        title: t.Optional[str] = ...,
        stylekit: t.Union[bool, Stylekit] = ...,
        upload_folder: t.Optional[str] = ...,
        use_arrow: bool = ...,
        use_reloader: bool = ...,
        watermark: t.Optional[str] = ...,
        webapp_path: t.Optional[str] = ...,
        port: int = ...,
    ) -> Flask | None: ...
    def reload(self) -> None: ...
    def stop(self) -> None: ...
