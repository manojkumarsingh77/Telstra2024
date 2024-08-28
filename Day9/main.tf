provider "azurerm" {
  features {}
  subscription_id = "d632f066-f3cb-4f12-b1cc-8189b299f3eb"
}

# Resource Group
resource "azurerm_resource_group" "rg" {
  name     = "unext-rg"
  location = "East US"
}

# SQL Server
resource "azurerm_mssql_server" "sql_server" {
  name                         = "unext-sqlserver2"
  resource_group_name          = azurerm_resource_group.rg.name
  location                     = azurerm_resource_group.rg.location
  version                      = "12.0"
  administrator_login          = "sqlad"
  administrator_login_password = "Bappamorya&7"

  # Public access to the SQL Server
  public_network_access_enabled = true

}

# SQL Database
resource "azurerm_mssql_database" "sql_db" {
  name           = "unext-db"
  server_id      = azurerm_mssql_server.sql_server.id
  sku_name       = "Basic"
  max_size_gb    = 2
}

# Firewall Rule to Allow Public Access
resource "azurerm_mssql_firewall_rule" "allow_all" {
  name     = "AllowAllIPs"
  server_id = azurerm_mssql_server.sql_server.id
  start_ip_address = "0.0.0.0"
  end_ip_address   = "255.255.255.255"
}

output "sql_server_name" {
  value = azurerm_mssql_server.sql_server.name
}

output "sql_database_name" {
  value = azurerm_mssql_database.sql_db.name
}
