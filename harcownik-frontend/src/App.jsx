import { Routes, Route, BrowserRouter } from "react-router-dom";
import Navbar from "react-bootstrap/Navbar";
import NetworkNotifier from "react-network-notifier";
import React from "react";

import About from "./components/about/About";
import User from "./components/user/User";
import Login from "./components/login/Login";
import RegisterScout from "./components/registerScout/RegisterScout";
import RaportViewing from "./components/raportViewing/raportViewing";
import RegisterAdmin from "./components/registerAdmin/RegisterAdmin";
import ResetPassword from "./components/resetPassword/ResetPassword";
import TeamMembers from "./components/teamMembers/TeamMembers";
import Home from "./components/home/Home";
import Badges from "./components/badges/Badges";
import MyNavbar from "./components/mynavbar/MyNavbar";
import Footer from "./components/footer/Footer";
import NotFound from "./components/notfound/NotFound";
import Raport from "./components/raport/Raport";
import UserRequests from "./components/userRequests/UserRequests";

function App() {
  return (
    <div className="d-flex flex-column" style={{ minHeight: "100vh" }}>
      <NetworkNotifier message="Ups, you lost internet conection" />
      <BrowserRouter>
        <MyNavbar />
        <Navbar />
        <div className="flex-grow-1 d-flex justify-content-center align-items-center">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/register_scout" element={<RegisterScout />} />
            <Route path="/raport_viewing" element={<RaportViewing />} />
            <Route path="/register_admin" element={<RegisterAdmin />} />
            <Route path="/reset_password" element={<ResetPassword />} />
            <Route path="/about" element={<About />} />
            <Route path="/user" element={<User />} />
            <Route path="/badges" element={<Badges />} />
            <Route path="/raport" element={<Raport />} />
            <Route path="/team_members" element={<TeamMembers />} />
            <Route path="/user_requests" element={<UserRequests />} />
            <Route path="*" element={<NotFound />} />
          </Routes>
        </div>
        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
