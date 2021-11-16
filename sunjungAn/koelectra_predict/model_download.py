import gdown
url = "https://drive.google.com/uc?id=1zjGH_9Lz1hl-geR1Cnau195ZNQthaJjQ"
output = "./koelectra_predict/koelectra-wellnesee-text-classification.pth"
gdown.download(url, output, quiet = False)