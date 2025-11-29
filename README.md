# Image Microservice

## How to request data
Send a json containing the image_url and size you want the output image to be (ex. 200 for a 200x200 image)
```
requests.post(
      "http://localhost:5001/api/cover/process",
      json={"image_url": test_url, "size": 200}
  )
```

## How to receive and use data
The microservice will respond with a json object. To extract the iamge data use `bytes.fromhex(response["image_data"])` and then write it to your desired file

```
{
  "status": "success",
  "image_data": hexadecimal string representing image,
  "dimensions": "200",
  "format": "JPEG"
}
```