provider "azurerm" {
  features{}
  subscription_id = "d632f066-f3cb-4f12-b1cc-8189b299f3eb"
}

# Resource Group
resource "azurerm_resource_group" "unext_rg" {
  name     = "unext-rg"
  location = "East US 2"
}

# Cosmos DB Account
resource "azurerm_cosmosdb_account" "unext_cosmosdb" {
  name                = "unext-cosmosdb-account"
  location            = azurerm_resource_group.unext_rg.location
  resource_group_name = azurerm_resource_group.unext_rg.name
  offer_type          = "Standard"
  kind                = "GlobalDocumentDB"

  consistency_policy {
    consistency_level = "Session"
  }

  geo_location {
    location          = azurerm_resource_group.unext_rg.location
    failover_priority = 0
  }

  capabilities {
    name = "EnableServerless"
  }

  public_network_access_enabled = true
}

# Cosmos DB SQL Database
resource "azurerm_cosmosdb_sql_database" "unext_sqldb" {
  name                = "unext-sqldb"
  resource_group_name = azurerm_resource_group.unext_rg.name
  account_name        = azurerm_cosmosdb_account.unext_cosmosdb.name
}

# Cosmos DB SQL Container
resource "azurerm_cosmosdb_sql_container" "unext_container" {
  name                = "unext-container"
  resource_group_name = azurerm_resource_group.unext_rg.name
  account_name        = azurerm_cosmosdb_account.unext_cosmosdb.name
  database_name       = azurerm_cosmosdb_sql_database.unext_sqldb.name
  
  # Correcting the partition_key_path argument to partition_key_paths
  partition_key_paths = ["/partitionKey"]

  indexing_policy {
    indexing_mode = "consistent"

    included_path {
      path = "/*"
    }

    excluded_path {
      path = "/\"_etag\"/?"
    }
  }
}
