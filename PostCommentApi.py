import json
import requests


class PostCommentApi:
    def posts_api(post_api_url):      
        try:
            post_response = requests.request("GET", post_api_url)
        except Exception as err:
            post_responce = ""    
        return post_response

    
    def commenst_api(comment_api_url):
        try:
            comment_response = requests.request("GET", comment_api_url)
        except Exception as err:
            comment_response = ""
        return comment_response

    
    def main_app():
        POST_API_URL = "https://my-json-server.typicode.com/typicode/demo/posts"
        COMMENT_API_URL = "https://my-json-server.typicode.com/typicode/demo/comments"
        postidJson = PostCommentApi.posts_api(POST_API_URL)
        commentApi = PostCommentApi.commenst_api(COMMENT_API_URL)
        if (postidJson.status_code==200 or  postidJson is not None) and (commentApi.status_code==200 or  commentApi is not None):
            postidJson = json.loads(postidJson.text)
            commentApi = json.loads(commentApi.text)
            post_comment_list = []
            for postId in postidJson:
                post_id = postId['id']
                commentv = []
                for comment in commentApi:
                    if post_id == comment['postId']:
                        commentv.append(comment['body'])
                post_comment_mapping =   {
                    "postId": post_id,
                    "comments": commentv,
                }

                post_comment_list.append(post_comment_mapping)
            return json.dumps(post_comment_list)
        else:
            return {"message": "Failed to merge post and comment" }

print(PostCommentApi.main_app())
