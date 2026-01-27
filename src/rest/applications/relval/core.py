"""
REST client for the RelVal application.
"""

from typing import Union

from rest.applications.base import BaseClient


class RelVal(BaseClient):
    """
    Initializes an HTTP client for querying RelVal.
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
        # Set the HTTP session
        super().__init__(
            app="relval",
            id=id,
            debug=debug,
            cookie=cookie,
            dev=dev,
            client_id=client_id,
            client_secret=client_secret,
        )

    # RelVal methods

    def create(self, data):
        """
        Create a new RelVal.
        Requires manager role.
        """
        return self._put(url="api/relvals/create", data=data)

    def delete(self, data):
        """
        Delete one or multiple RelVals.
        Requires manager role.
        """
        return self._delete(url="api/relvals/delete", data=data)

    def update(self, data):
        """
        Update one or multiple RelVals.
        Requires manager role.
        """
        return self._post(url="api/relvals/update", data=data)

    def get_relval(self, prepid: str):
        """
        Retrieve a single RelVal by its prepid.
        """
        return self._get(url=f"api/relvals/get/{prepid}")

    def get_editable(self, prepid: str = None):
        """
        Get information on which RelVal fields are editable.
        If prepid is given, return for a specific RelVal.
        """
        url = "api/relvals/get_editable"
        if prepid:
            url += f"/{prepid}"
        return self._get(url=url)

    def get_cmsdriver(self, prepid: str):
        """
        Get a bash script with cmsDriver.py commands of RelVal.
        """
        return self._get(url=f"api/relvals/get_cmsdriver/{prepid}")

    def get_config_upload(self, prepid: str):
        """
        Get a bash script to upload configs to ReqMgr config cache.
        """
        return self._get(url=f"api/relvals/get_config_upload/{prepid}")

    def get_dict(self, prepid: str):
        """
        Get a dictionary with job information for ReqMgr2.
        """
        return self._get(url=f"api/relvals/get_dict/{prepid}")

    def get_default_step(self):
        """
        Get a default (empty) step that could be used as a template.
        """
        return self._get(url="api/relvals/get_default_step")

    def next_status(self, data):
        """
        Move one or multiple RelVals to next status.
        Requires manager role.
        """
        return self._post(url="api/relvals/next_status", data=data)

    def previous_status(self, data):
        """
        Move one or multiple RelVals to previous status.
        Requires manager role.
        """
        return self._post(url="api/relvals/previous_status", data=data)

    def update_workflows(self, data):
        """
        Trigger one or multiple RelVal updates from Stats2 (ReqMgr2 + DBS).
        Requires manager role.
        """
        return self._post(url="api/relvals/update_workflows", data=data)
        
    ## Tickets methods
    def create_ticket(self, data):
        """
        Create a new RelVal ticket.
        Requires manager role.
        """
        return self._put(url="api/ticket/create", data=data)
