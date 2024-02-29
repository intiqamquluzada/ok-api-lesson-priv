class Uploader:

    @staticmethod
    def upload_photo_index(instance, filename):
        return f"index/{filename}"

    @staticmethod
    def upload_photo_index1(instance, filename):
        return f"index/{filename}"  
    
    @staticmethod
    def upload_photo_projects(instance, filename):
        return f" projects/{filename}" 
    
    @staticmethod
    def upload_photo_partniors(instance, filename):
        return f" partniors/{filename}" 

    @staticmethod
    def upload_photo_blog(instance, filename):
        return f" blog/{filename}" 
    
    @staticmethod
    def upload_photo_about(instance, filename):
        return f" about/{filename}" 
    
    
