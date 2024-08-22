# Cisco AXL Services with Python

Using Cisco AXL Services with Python.

You can download **AXLAPI.wsdl** and **AXLSoap.xsd** files from **CUCM > Application > Plugins > Cisco AXL Plugins** section.

## Package Requirements

Zeep

## Examples

### Listing Phones

You can filter the search by specifying the allowed arguments in **search_criteria**.

Likewise, **returned_tags** can be used to filter the fields to be shown in the results.

### Adding Phones

We define all the arguments we want, especially the required fields, in the **add_phone_data** variable. After adding, it returns device's uuid.

### Updating Phones

After defining the **uuid** or **name** of the device whose information we want to change, we define all the arguments we want to update in **update_phone_data**. 
If you want to trigger **Apply Config**, use this command: **service.applyPhone(name='PHONENAME')**
