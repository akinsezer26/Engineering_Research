Projenin çalıştırılabilmesi için bilgisayarda Openpose, OpenCV(ver. 3.4.3) ve Caffe yüklü olmalıdır.
OpenPose kütüphanesi --> https://github.com/CMU-Perceptual-Computing-Lab/openpose 
Caffe		      --> http://caffe.berkeleyvision.org/
OpenCV		      --> https://github.com/opencv/opencv/releases/tag/3.4.3
Cuda 8.0	      --> https://developer.nvidia.com/cuda-80-ga2-download-archive
Cudnn 5.1	      --> https://developer.nvidia.com/cudnn

Projede yer alan kodlar ve işlevleri
createModel.py	      --> Data.csv dosyasındaki verileri eğiterek bir model oluşturur.
testModel.py	      --> Örnek olarak çekilmiş video verilerinin bulunduğu dataTest.csv'yi kullanarak modeli test eder.
mp4ToJson.py	      --> Verilen klasördeki videoları openpose yardımıyla işleyerek JSON formatına dönüştürür(saatler süren bir işlem).
JsonToCsv.py	      --> Oluşturulan Json dosyalarını tek bir .csv'de(Data.csv veya test.csv gibi) birleştirir
testWebcam.py	      --> Webcami ve openpose'u ve monitor output kodunu açarak gerçek zamanlı hareket analizi yapar.
monitorOutput.py     --> Döngü halinde webcamden gelen verileri model ile karşılaştırıp predict yapar.Sonucu terminal ekranına yazdırır.

ÖNEMLİ NOT: PROJE UBUNTU 16.04 ÜZERİNDE YAPILMIŞ VE TEST EDİLMİŞTİR!!
