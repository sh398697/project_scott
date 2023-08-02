import React from "react";
import Post from "./Post";

function Posts({ posts, setPosts }) {

    const postObjArray = posts.map( postObj => {
        return <Post key={postObj.id} post={postObj} />
      } )

    return (
        <div>
            <br />
            <div>Posts:</div>
            <br />
            <div>{postObjArray}</div>
        </div>
  );
}

export default Posts;
