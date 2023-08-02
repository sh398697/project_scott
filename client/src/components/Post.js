import React from "react";

function Post({ post }) {



    return (
        <div>
            <div>{post.id}</div>
            <div>{post.title}</div>
            <div>{post.content}</div>
            <div>{post.userId}</div>
        </div>
  );
}

export default Post;
