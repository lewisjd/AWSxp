import boto3

def search_faces_by_image(bucket, key, collection_id, threshold=80, region="us-west-2"):
    rekognition = boto3.client("rekognition", region)
    
    response = rekognition.search_faces_by_image(
        CollectionId=collection_id,
        Image={
            "S3Object": {
                "Bucket": bucket,
                "Name": key,
            }
        },
        FaceMatchThreshold=threshold,
    )
    
    face_matches = response['FaceMatches']
    
    print(f"Matching faces")
    for match in face_matches:
        print(f"FaceId: {match['Face']['FaceId']}")
        print(f"Similarity: {match['Similarity']}")

    if not face_matches:
        print("No matches found")

# Assuming you already have a bucket and an image key (file path)
bucket = "your_bucket_name"
key = "your_image_file"
collection_id = "your_collection_id"

# Call the function
search_faces_by_image(bucket, key, collection_id)
