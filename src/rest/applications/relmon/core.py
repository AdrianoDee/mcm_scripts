"""
REST client for the RelMonService application.
"""

from typing import Union, Optional, Dict, Any
from urllib.parse import urlencode

from rest.applications.base import BaseClient


class RelMonService(BaseClient):
    """
    Initializes an HTTP client for querying RelMonService.
    """

    def __init__(
        self,
        id: str = BaseClient.SSO,
        debug: bool = False,
        cookie: Union[str, None] = None,
        dev: bool = True,
        client_id: str = "",
        client_secret: str = "",
    ):
        super().__init__(
            app="relmonservice",
            id=id,
            debug=debug,
            cookie=cookie,
            dev=dev,
            client_id=client_id,
            client_secret=client_secret,
        )

    # -----------------
    # RelMonService APIs
    # -----------------

    def get_relmons(
        self,
        page: int = 0,
        limit: Optional[int] = None,
        query: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        Fetch RelMons from database.
        """
        params = {"page": page}
        if limit is not None:
            params["limit"] = limit
        if query:
            params["q"] = query

        qs = f"?{urlencode(params)}" if params else ""
        return self._get(url=f"api/get_relmons{qs}")

    def create(self, relmon: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a new RelMon.
        """
        return self._post(url="api/create", data=relmon)

    def reset(self, relmon_id: str) -> Dict[str, Any]:
        """
        Reset a RelMon by ID.
        """
        return self._post(url="api/reset", data={"id": relmon_id})

    def delete(self, relmon_id: str) -> Dict[str, Any]:
        """
        Delete a RelMon by ID.
        """
        # DELETE in BaseClient does not take body, so we append id in query
        # or, if backend expects JSON body, we can emulate with requests directly
        # But since BaseClient._delete just calls session.delete, we must construct
        # the URL properly.
        return self._delete(url=f"api/delete?id={relmon_id}")

    def edit(self, relmon: Dict[str, Any]) -> Dict[str, Any]:
        """
        Edit an existing RelMon.
        """
        return self._post(url="api/edit", data=relmon)

    def update(self, relmon_update: Dict[str, Any]) -> Dict[str, Any]:
        """
        Update RelMon info (status, categories, etc).
        Requires service account role.
        """
        return self._post(url="api/update", data=relmon_update)

    def tick(self) -> Dict[str, Any]:
        """
        Trigger a controller tick.
        """
        return self._get(url="api/tick")

    def user(self) -> Dict[str, Any]:
        """
        Get user info.
        """
        return self._get(url="api/user")
