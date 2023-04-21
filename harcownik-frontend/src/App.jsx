import { Routes, Route, BrowserRouter } from "react-router-dom";
import Navbar from "react-bootstrap/Navbar";
import React from "react";

import About from './components/about/About';
import User from './components/user/User';
import Home from './components/home/Home';
import Badges from './components/badges/Badges';
import MyNavbar from './components/mynavbar/MyNavbar';
import Footer from './components/footer/Footer';
import NotFound from './components/notfound/NotFound';
import Raport from './components/raport/Raport';
import RaportViev from './components/raport/RaportViev'

function App() {
  return (
    <div className="d-flex flex-column" style={{ minHeight: "100vh"}}>
      <BrowserRouter>
        <MyNavbar />
        <Navbar />
        <div className="flex-grow-1 d-flex justify-content-center align-items-center">
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/user" element={<User />} />
            <Route path="/badges" element={<Badges />} />
            <Route path="/raport" element={<Raport/>} />
            <Route path="*" element={<NotFound />} />
            <Route path="/raport/raport_viev" element={<RaportViev />} />

          </Routes>
        </div>
        <Footer />
      </BrowserRouter>
    </div>
  );
}

export default App;
