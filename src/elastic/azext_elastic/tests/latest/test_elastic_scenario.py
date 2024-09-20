# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from azure.cli.testsdk import *


class ElasticScenario(ScenarioTest):
    @ResourceGroupPreparer(name_prefix='cli_test_elastic_monitor', location='eastus')
    def test_elastic_monitor(self, resource_group):
        email = self.cmd('account show').get_output_in_json()['user']['name']
        self.kwargs.update({
            'monitor': self.create_random_name('monitor', 20),
            'email': email
        })
        self.cmd('elastic monitor create -n {monitor} -g {rg} --user-info {{firstName:Alice,lastName:bob,companyName:Micosoft,emailAddress:{email}}} --sku {{name:ess-monthly-consumption_Monthly}}', checks=[
            self.check('name', '{monitor}'),
            self.check('resourceGroup', '{rg}'),
            self.check('sku.name', 'ess-monthly-consumption_Monthly')
        ])
        self.cmd('elastic monitor update -n {monitor} -g {rg} --tags {{tag:test,tag2:test2}}', checks=[
            self.check('name', '{monitor}'),
            self.check('resourceGroup', '{rg}'),
            self.check('tags.tag', 'test'),
            self.check('tags.tag2', 'test2')
        ])
        self.cmd('elastic monitor list -g {rg}', checks=[
            self.check('[0].name', '{monitor}'),
            self.check('[0].resourceGroup', '{rg}'),
            self.check('[0].sku.name', 'ess-monthly-consumption_Monthly')
        ])
        self.cmd('elastic monitor show -n {monitor} -g {rg}', checks=[
            self.check('name', '{monitor}'),
            self.check('resourceGroup', '{rg}'),
            self.check('sku.name', 'ess-monthly-consumption_Monthly')
        ])
        self.cmd("elastic monitor create-or-update-external-user --monitor-name {monitor} -g {rg} --user-name newuser --full-name fullname --password password --email-id email@outlook.com --roles [admin,other_role]", checks=[self.check('created', True)])
        self.cmd('elastic monitor list-all-traffic-filter --monitor-name {monitor} -g {rg}', checks=[
            self.check('length(@)', 1)
        ])
        self.cmd('elastic monitor list-associated-traffic-filter --monitor-name {monitor} -g {rg}', checks=[
            self.check('length(@)', 1)
        ])
        self.cmd('elastic monitor list-deployment-info --monitor-name {monitor} -g {rg}', checks=[
            self.check('status', 'Healthy')
        ])
        self.cmd('elastic monitor list-connected-partner-resource --monitor-name {monitor} -g {rg}', checks=[
            self.check('type(@)', 'array')
        ])
        self.cmd('elastic monitor get-billing-info --monitor-name {monitor} -g {rg}', checks=[
                 self.check('length(marketplaceSaasInfo)', 5)
        ])
        self.cmd('elastic monitor list-resource --monitor-name {monitor} -g {rg}')
        self.cmd('elastic monitor list-upgradable-version --monitor-name {monitor} -g {rg}')
        self.cmd('elastic monitor list-vm-host --monitor-name {monitor} -g {rg}')
        self.cmd('elastic monitor detach-and-delete-traffic-filter --monitor-name {monitor} -g {rg}')
        self.cmd('elastic monitor delete-traffic-filter --monitor-name {monitor} -g {rg}')
        self.cmd('elastic monitor upgrade --monitor-name {monitor} -g {rg} --version 8.0.0'),
        self.cmd('elastic monitor create-and-associate-ip-filter --monitor-name {monitor} -g {rg} --name filter1 --ips "192.168.131.0, 192.168.132.6/22"')
        self.cmd('elastic monitor create-and-associate-pl-filter --monitor-name {monitor} -g {rg} --name filter2'),
        self.cmd('elastic monitor delete-traffic-filter --monitor-name {monitor} -g {rg}')

        self.cmd('elastic monitor delete -n {monitor} -g {rg} -y')

    @ResourceGroupPreparer(name_prefix='cli_test_elastic_monitor', location='eastus')
    def test_elastic_monitor_tag_rule(self, resource_group):
        email = self.cmd('account show').get_output_in_json()['user']['name']
        self.kwargs.update({
            'monitor': self.create_random_name('monitor', 20),
            'email': email
        })
        self.cmd('elastic monitor create -n {monitor} -g {rg} --user-info {{firstName:Alice,lastName:bob,companyName:Micosoft,emailAddress:{email}}} --sku {{name:ess-monthly-consumption_Monthly}}', checks=[
            self.check('name', '{monitor}'),
            self.check('resourceGroup', '{rg}'),
            self.check('sku.name', 'ess-monthly-consumption_Monthly'),
        ])
        self.cmd('elastic monitor tag-rule create -n default -g {rg} --monitor-name {monitor} --log-rules {{filteringTags:[{{name:Environment,value:Prod,action:Include}}]}}', checks=[
            self.check('name', 'default'),
            self.check('resourceGroup', '{rg}'),
            self.check('properties.logRules.filteringTags[0].action', 'Include'),
            self.check('properties.logRules.filteringTags[0].name', 'Environment'),
            self.check('properties.logRules.filteringTags[0].value', 'Prod'),
            self.check('properties.logRules.sendAadLogs', False),
            self.check('properties.logRules.sendActivityLogs', False),
            self.check('properties.logRules.sendSubscriptionLogs', False)
        ])
        self.cmd('elastic monitor tag-rule update -n default -g {rg} --monitor-name {monitor} --log-rules {{filteringTags:[{{name:Environment2,value:Prod,action:Include}}]}}', checks=[
            self.check('name', 'default'),
            self.check('resourceGroup', '{rg}'),
            self.check('properties.logRules.filteringTags[0].action', 'Include'),
            self.check('properties.logRules.filteringTags[0].name', 'Environment2'),
            self.check('properties.logRules.filteringTags[0].value', 'Prod'),
            self.check('properties.logRules.sendAadLogs', False),
            self.check('properties.logRules.sendActivityLogs', False),
            self.check('properties.logRules.sendSubscriptionLogs', False)
        ])
        self.cmd('elastic monitor tag-rule list -g {rg} --monitor-name {monitor}', checks=[
            self.check('[0].name', 'default'),
            self.check('[0].resourceGroup', '{rg}'),
            self.check('[0].properties.logRules.filteringTags[0].action', 'Include'),
            self.check('[0].properties.logRules.filteringTags[0].name', 'Environment2'),
            self.check('[0].properties.logRules.filteringTags[0].value', 'Prod'),
            self.check('[0].properties.logRules.sendAadLogs', False),
            self.check('[0].properties.logRules.sendActivityLogs', False),
            self.check('[0].properties.logRules.sendSubscriptionLogs', False)
        ])
        self.cmd('elastic monitor tag-rule show -n default -g {rg} --monitor-name {monitor}', checks=[
            self.check('name', 'default'),
            self.check('resourceGroup', '{rg}'),
            self.check('properties.logRules.filteringTags[0].action', 'Include'),
            self.check('properties.logRules.filteringTags[0].name', 'Environment2'),
            self.check('properties.logRules.filteringTags[0].value', 'Prod'),
            self.check('properties.logRules.sendAadLogs', False),
            self.check('properties.logRules.sendActivityLogs', False),
            self.check('properties.logRules.sendSubscriptionLogs', False)
        ])
    @ResourceGroupPreparer(name_prefix='cli_test_elastic_monitor', location='eastus')
    def test_elastic_monitor_open_ai_integration(self, resource_group):
        email = self.cmd('account show').get_output_in_json()['user']['name']
        self.kwargs.update({
            'monitor': self.create_random_name('monitor', 20),
            'email': email
        })
        self.cmd('elastic monitor create -n {monitor} -g {rg} --user-info {{firstName:Alice,lastName:bob,companyName:Micosoft,emailAddress:{email}}} --sku {{name:ess-monthly-consumption_Monthly}}', checks=[
            self.check('name', '{monitor}'),
            self.check('resourceGroup', '{rg}'),
            self.check('sku.name', 'ess-monthly-consumption_Monthly'),
        ])
        self.cmd('elastic monitor open-ai-integration create -n default -g {rg} --monitor-name {monitor} --key {api_key} --open-ai-connector-id {connector_id} --open-ai-resource-endpoint {endpoint} --open-ai-resource-id {resource_id}', checks=[
            self.check('name', 'default'),
            self.check('resourceGroup', '{rg}'),
            self.check('properties.key', '{api_key}'),
            self.check('properties.openAIConnectorId', '{connector_id}'),
            self.check('properties.openAIResourceEndpoint', '{endpoint}'),
            self.check('properties.openAIResourceId', '{resource_id}'),
        ])
        self.cmd('elastic monitor open-ai-integration update -n default -g {rg} --monitor-name {monitor} --key {openai_key} --open-ai-connector-id {connector_id} --open-ai-resource-endpoint {resource_endpoint} --open-ai-resource-id {resource_id}', checks=[
            self.check('name', 'default'),
            self.check('resourceGroup', '{rg}'),
            self.check('properties.key', '{openai_key}'),
            self.check('properties.openAIConnectorId', '{connector_id}'),
            self.check('properties.openAIResourceEndpoint', '{resource_endpoint}'),
            self.check('properties.openAIResourceId', '{resource_id}')
        ])
        self.cmd('elastic monitor open-ai-integration list -g {rg} --monitor-name {monitor}', checks=[
            self.check('[0].name', 'openAIIntegrationRule1'),
            self.check('[0].properties.open_ai_connector_id', 'connectorID1'),
            self.check('[0].properties.open_ai_resource_id', 'resourceID1'),
            self.check('[0].properties.open_ai_resource_endpoint', 'https://openai.endpoint'),
            self.check('[0].properties.last_refresh_at', '2024-09-20T00:00:00Z'),
            self.check('[0].type', 'Microsoft.Elastic/monitors/openAIIntegrations')
        ])
        self.cmd('elastic monitor open-ai-integration show -n default -g {rg} --monitor-name {monitor}', checks=[
            self.check('name', 'default'),
            self.check('resourceGroup', '{rg}'),
            self.check('properties.openAIConnectorId', '{open_ai_connector_id}'),
            self.check('properties.openAIResourceEndpoint', '{open_ai_resource_endpoint}'),
            self.check('properties.openAIResourceId', '{open_ai_resource_id}'),
            self.check('properties.lastRefreshAt', '{last_refresh_at}')
        ])




