import requests, json
import os
import sys

class FL_model():
    #0-0. Define the AI ​​model repository address 
    base_url = "http://0.0.0.0:8080/"
    
    def __init__(self, url):
        self.base_url=url
        
    def set_model_info(self, model_info):
        self.model_info = model_info
        
    def set_upload_file_name(self, upload_file_name):
        self.upload_file_name = upload_file_name
    
    def set_stored_file_name(self, stored_file_name):
        self.stored_file_name = stored_file_name
        
    def model_upload(self):

        model_path= requests.post(self.base_url+'FL_upload_path_make', data=json.dumps(self.model_info))#FL_model_upload(model_info, upload_file_name, base_url)
        file_name = self.model_info['device_name']+'_data.zip'
        files ={'file':(file_name, open(self.upload_file_name,'rb'))}
        fl_model_url = self.base_url+"Model_upload_FL?folder="+model_path.text
        upload_response = requests.post(url=fl_model_url, files = files)
        print("Upload URL:", upload_response.text)
    
    def model_download(self):
        
        download_url= self.base_url+"model_download_FL?"
        # 2-2. Make REST API address based on model information.
        for key in self.model_info:
            download_url +=key+'='+self.model_info[key]+'&'
        #http://182.252.132.39:5000/model_download_FL?model_name=decenter_mnist&model_version=0.1&model_location=server&device_name=keti
        print("Download URL:", download_url)
        
        # 2-3. Download and Save
        FL_model = requests.get(download_url)
        return FL_model
        
    
    def model_save(self, Fl_model):
        try:
            print(self.stored_file_name)
            print(self.stored_file_name, "start")
            f = open(self.stored_file_name,'wb')
            f.write(Fl_model.content)
            print(self.stored_file_name, "is stored on local storage.")
        except:
            sys.stderr.write("No file: %s", self.stored_file_name)
            exit(1)
            
        f.close()
