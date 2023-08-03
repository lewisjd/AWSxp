import boto3

s3 = boto3.resource('s3')

images =  [('1.JPEG', 'Lionel Messi'),
           ('2.PNG', 'Cristiano Ronaldo'),
           ('3.JPEG', 'Elon Musk'),
           ('4.JPEG', ' Donald Trump'),
           ('5.JPEG', 'Boris Johnson')]

for image in images:
    file = open(image[0],'rb')
    object = s3.Object('rekognitionfacecollection','index2/'+ image[0])
    ret = object.put(Body=file,
                     Metadata={'FullName':image[1]}
                     )
           
