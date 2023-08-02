import React from "react";

function UserCard({ user }) {



    return (
        <div>
            <div>User ID: {user.id}</div>
            <div>Name: {user.fname} {user.lname}</div>
            <div>Email: {user.email}</div>
            <div>Phone: {user.phone}</div>
            <div>Image: {user.image_url}</div>
            <br />
        </div>
  );
}

export default UserCard;
