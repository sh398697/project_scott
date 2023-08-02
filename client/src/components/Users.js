import React from "react";
import UserCard from "./UserCard";

function Users({ users }) {

    const userObjArray = users.map( userObj => {
        return <UserCard key={userObj.id} team={userObj} />
      } )

    return (
        <div>
            <br />
            <div>Users:</div>
            <br />
            <div>{userObjArray}</div>
        </div>
  );
}

export default Users;
