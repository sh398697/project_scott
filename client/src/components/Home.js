import React from "react";
import UserCard from "./UserCard";

function Home({ users }) {

    const userObjArray = users.map( userObj => {
        return <UserCard key={userObj.id} team={userObj} />
      } )

    return (
        <div>
            <div>{userObjArray}</div>
        </div>
  );
}

export default Home;
