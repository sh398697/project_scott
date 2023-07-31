import React from "react";

function UserCard({ team }) {



    return (
        <div>
            <div>User ID: {team.id}</div>
            <div>Name: {team.fname} {team.lname}</div>
            <div>Email: {team.email}</div>
            <div>Phone: {team.phone}</div>
            <div>Image: {team.image_url}</div>
            <br />
        </div>
  );
}

export default UserCard;
