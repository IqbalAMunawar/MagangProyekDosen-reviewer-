from django.db import models
from django.urls import reverse

class Segmentasi_dataset(models.Model):
    id_segmentasi_dataset = models.AutoField(primary_key=True)
    id_hasi_dataset = models.IntegerField()
    id_tipe_segmentasi = models.IntegerField()
    label_segmentasi = models.CharField(max_length=20)
    warna_segmentasi = models.CharField(max_length=20)
    koordinat = models.TextField()
    
class Direktori(models.Model):
    id_direktori = models.AutoField(primary_key=True)
    alamat_direktori = models.CharField(max_length=200)

class Gambar(models.Model):
    id_gambar = models.AutoField(primary_key=True)
    id_pengguna = models.IntegerField()
    id_direktori = models.IntegerField()
    id_dataset = models.IntegerField()
    nama_file = models.CharField(max_length=255)
    ukuran_file = models.BigIntegerField()
    tanggal_dibuat = models.DateTimeField(auto_now_add=True)
    format_file = models.CharField(max_length=50)
    tanggal_pengambilan = models.DateTimeField()
    model_kamera = models.CharField(max_length=255)
    lebar = models.IntegerField()
    tinggi = models.IntegerField()
    lokasi_pengambilan = models.CharField(max_length=255)
    id_pembuat = models.IntegerField()
    tanggal_buat = models.DateTimeField(auto_now_add=True)
    
class Gamabar_dataset(models.Model):
    id_gambar_dataset = models.AutoField(primary_key=True)
    id_gambar = models.IntegerField()
    id_profile_dataset = models.IntegerField()
    is_training = models.BooleanField()
       
class profile_job(models.MOdel):
    
class job_item(models.Model):
    id_job_item = models.AutoField(primary_key=True)
    id_profile_job = models.IntegerField()
    id_gambar = models.IntegerField()
    id_job_segmentasi_annotator = models.IntegerField()
    id_job_segmentasi_reviewer = models.IntegerField()
    status_pekerjaan = models.CharField(max_length=50)
    

class Tipe_segmentasi(models.model):
    id_tipe_segmentasi = models.AutoField(primary_key=True)
    nama_tipe_segmentasi = models.CharField(max_length=50)

class Segmentasi_detail(models.Model) :
    id_segmentasi_detai = models.AutoField(primary_key=True)
    id_segmentasi = models.IntegerField()
    koordinat_x = models.FloatField()
    koordinat_y = models.FloatField()
    
class Segmentasi(models.Model):
    id_tipe_segmentasi = models.AutoField(primary_key=True)
    id_tipe_segmentasi = models.IntegerField()
    label_segmentasi = models.CharField(max_length=20)
    warna_segmentasi = models.CharField(max_length=10)
    koordinat = models.TextField()
    id_job_item = models.IntegerField()

class Anotasi(models.Model):
    id_anotasi = models.AutoField(primary_key=True)
    id_segmentasi = models.IntegerField()
    id_gambar = models.IntegerField()
    koordinat_x = models.FloatField()
    koordinat_y = models.FloatField()
    lebar = models.FloatField()
    tinggi = models.FloatField()
    
class IssueAnnotation(models.Model):
    id = models.AutoField(primary_key=True)
    issue_date = models.DateField()
    message = models.TextField()  # assuming it's a text field, not just a str
    issue_type_name = models.CharField(max_length=255)  # assuming a reasonable max length
    issue_annotation_parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

class IssueImage(models.Model):
    id = models.AutoField(primary_key=True)
    creator_id = models.IntegerField()  # assuming it's an integer, not a User model
    create_date = models.DateField()
    message = models.TextField()  # assuming it's a text field, not just a str
    issue_type_name = models.CharField(max_length=255)  # assuming a reasonable max length
    issue_parent_image = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

class IssueSegmentation(models.Model):
    id_segmentation = models.AutoField(primary_key=True)
    id_image = models.ForeignKey(IssueImage, on_delete=models.CASCADE)
    coordinate_x = models.FloatField()
    coordinate_y = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()