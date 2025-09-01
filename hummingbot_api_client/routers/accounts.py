from typing import Optional, Dict, Any, List
from .base import BaseRouter


class AccountsRouter(BaseRouter):
    """Accounts router for account and credential management operations."""
    
    # Account Operations
    async def list_accounts(self) -> List[str]:
        """List all account names."""
        return await self._get("/accounts/")
    
    async def add_account(self, account_name: str) -> Dict[str, Any]:
        """Create new account."""
        return await self._post("/accounts/add-account", params={"account_name": account_name})
    
    async def delete_account(self, account_name: str) -> Dict[str, Any]:
        """Delete account."""
        return await self._post("/accounts/delete-account", params={"account_name": account_name})
    
    # Credentials Management
    async def list_account_credentials(self, account_name: str) -> List[str]:
        """List connector names that have credentials configured for an account."""
        return await self._get(f"/accounts/{account_name}/credentials")
    
    async def add_credential(
        self,
        account_name: str,
        connector_name: str,
        credentials: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Add or update connector credentials for an account."""
        return await self._post(
            f"/accounts/add-credential/{account_name}/{connector_name}",
            json=credentials
        )
    
    async def delete_credential(self, account_name: str, connector_name: str) -> Dict[str, Any]:
        """Delete connector credentials for an account."""
        return await self._post(f"/accounts/delete-credential/{account_name}/{connector_name}")
    
    # Config Management
    async def list_accounts_configs(self, account_name: str) -> List[str]:
        """Get a list of all config names for an account."""
        return await self._get(f"/accounts/{account_name}/configs")

    async def get_account_config(
        self, account_name: str, config_name: str
    ) -> Dict[str, Any]:
        """Get a specific client config for an account by the config folder name."""
        return await self._get(f"/accounts/{account_name}/config/{config_name}")

    async def add_account_config(
        self, account_name: str, config_name: str
    ) -> Dict[str, Any]:
        """Add a new, empty config folder for a specific account."""
        return await self._post(
            f"/accounts/{account_name}/add-config",
            params={"config_name": config_name},
        )

    async def update_account_config(
        self, account_name: str, config_name: str, client_config: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Update the client config for a specific account and config folder."""
        return await self._post(
            f"/accounts/{account_name}/update-config",
            params={"config_name": config_name},
            json={"client_config": client_config},
        )

    async def delete_account_config(
        self, account_name: str, config_name: str
    ) -> Dict[str, Any]:
        """Delete a config folder for a specific account."""
        return await self._post(
            f"/accounts/{account_name}/delete-config",
            params={"config_name": config_name},
        )
