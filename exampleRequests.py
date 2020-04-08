from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
import pdb

# Configure API key authorization: ApiKeyAuth
configuration = swagger_client.Configuration()
configuration.api_key['x-api-key'] = '<ENTER API KEY HERE>'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x-api-key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ModelConfigurationsApi(swagger_client.ApiClient(configuration))

layer1 = swagger_client.Layer(1000, 4000, 2000)
layer2 = swagger_client.Layer(500, 3000, 1500)

density_layer1 = swagger_client.DensityLayer(1000, 250)
density_layer2 = swagger_client.DensityLayer(500, 550)
body = swagger_client.ParamSet('EagleFord', 100, 200, 300, 'Elastic', 2000, 100, [layer1, layer2], [density_layer1, density_layer2]) # ParamSet | Model Configuration to add (optional)

# UNCOMMENT REQUESTS BELOW TO TEST

#### GET ALL MODEL CONFIGURATIONS FOR USER

# try:
#     # Returns all of a users model configurations.
#     api_response = api_instance.get_configurations()
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling ModelConfigurationsApi->get_configurations: %s\n" % e)

#### CREATE A MODEL ######

# try:
#     # Creates a model configuration.
#     api_response = api_instance.create_configuration(body=body)
#     pprint(api_response)

# except ApiException as e:
#     print("Exception when calling ModelConfigurationsApi->create_configuration: %s\n" % e)

#### GET A MOEL FROM THE ID *******

# id = '5e8c0ce5956c3b00360c50fb' # str | 
# status_only = 'false' # can be true or false, or just leave off. Save some network bandwidth if you just
# # to poll for the status of a model.

# try:
#     # Returns a model configuration
#     api_response = api_instance.get_configuration(id, status_only=status_only)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling ModelConfigurationsApi->get_configuration: %s\n" % e)

# pdb.set_trace()


####### UPDATE A MODEL ###########

# id = '5e8c0ce5956c3b00360c50fb' # str | 
# body = swagger_client.ParamSet('EagleFord_CHANGED_THE_NAME_ARGO_BLARGO', 100, 200, 300, 'Elastic', 2000, 100, [layer1, layer2], [density_layer1, density_layer2]) # ParamSet | Model Configuration to add (optional)

# try:
#     # Update and replace a model configuration
#     api_response = api_instance.update_configuration(id, body=body)
#     pprint(api_response)
# except ApiException as e:
#     print("Exception when calling ModelConfigurationsApi->update_configuration: %s\n" % e)

####### LAUNCH A JOB FOR PROCESSING ##############

# id = '5e8c0ce5956c3b00360c50fb' # str | 

# try:
#     # Launch a configuration to one of the workers to be processed.
#     api_instance.launch_configuration(id)
# except ApiException as e:
#     print("Exception when calling ModelConfigurationsApi->launch_configuration: %s\n" % e)

###### RETREIVE SIGNED URL TO DOWNLOAD BINARY

# id = '5e8c0ce5956c3b00360c50fb' # str | 

# try:
#     # Retreive signed url to download binary
#     api_response = api_instance.download_configuration(id)
#     pprint(api_response)

# except ApiException as e:
#     print("Exception when calling ModelConfigurationsApi->download_configuration: %s\n" % e)

