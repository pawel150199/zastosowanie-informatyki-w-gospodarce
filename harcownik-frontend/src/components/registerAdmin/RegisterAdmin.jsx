/* eslint-disable */
import React, { useState, useEffect } from "react";
import { View, Text, TextInput, TouchableOpacity } from "react-native";
import { Button } from "react-bootstrap";
import { Link } from "react-router-dom";

import axios from "../../api/api"
import authHeader from "../../api/authHeader";
import addAdmin from "./addAdmin";
import addGroup from "./addGroup";

import styles from "./RegisterAdminStyle";

const RegisterAdmin = () => {
  // Team Admin
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [level, setLevel] = useState("");
  const [func, setFunc] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  // Group
  const [name, setName] = useState("");
  const [number, setNumber] = useState("");
  const [szczep, setSzczep] = useState("");
  const [city, setCity] = useState("");
  const [groupId, setGroupId] = useState("");

  // Info
  // eslint-disable-next-line
  const [info, setInfo] = useState(" ");

  useEffect(() => {
    handleRegisterAdmin();
  },[]);

  const handleRegisterAdmin = async () => {
    try {
      const group = await addGroup(name, number, szczep, city);
      const admin = await addAdmin(firstName, lastName, email, level, func, password, confirmPassword, group.data.id);
      setInfo("Drużynowy i grupa stworzono pomyślnie!");
      window.location.href = "/login";
    } catch (error) {
      setInfo("Wystąpił błąd!");
      console.error(error);
    }
  };

  return (
    <View style={styles.container}>
      <small>{info}</small>
      <br></br>
      <Text style={styles.title}>Załóż nową drużynę Harcerską</Text>
      <small>Jeśli twoja dryżyna jest już w aplikacji harcownik, poproś swojego drużynowego o dodanie :)</small>
      <br></br>
      <TextInput
        style={styles.input}
        placeholder="Nazwa Drużyny"
        value={name}
        onChangeText={setName}
      />
      <TextInput
        style={styles.input}
        placeholder="Numer drużyny"
        value={number}
        onChangeText={setNumber}
      />
      <TextInput
        style={styles.input}
        placeholder="Nazwa Szczepu Drużyny"
        value={szczep}
        onChangeText={setSzczep}
      />
      <TextInput
        style={styles.input}
        placeholder="Miasto Drużyny"
        value={city}
        onChangeText={setCity}
      />


      <br></br>
      <Text style={styles.title}>Załóż konto Drużynowego</Text>
      <small>Konto Drużynowego zostanie automatycznie zostanie dodane do drużyny</small>
      <br></br>
      <TextInput
        style={styles.input}
        placeholder="Imie"
        value={firstName}
        onChangeText={setFirstName}
      />
      <TextInput
        style={styles.input}
        placeholder="Nazwisko"
        value={lastName}
        onChangeText={setLastName}
      />
      <TextInput
        style={styles.input}
        placeholder="Poziom harcerza"
        value={level}
        onChangeText={setLevel}
      />
      <TextInput
        style={styles.input}
        placeholder="Funkcja harcerza"
        value={func}
        onChangeText={setFunc}
      />
      <TextInput
        style={styles.input}
        placeholder="Adres email"
        keyboardType="email-address"
        value={email}
        onChangeText={setEmail}
      />
      <TextInput
        style={styles.input}
        placeholder="Hasło"
        secureTextEntry={true}
        value={password}
        onChangeText={setPassword}
      />
      <TextInput
        style={styles.input}
        placeholder="Powtórz hasło"
        secureTextEntry={true}
        value={confirmPassword}
        onChangeText={setConfirmPassword}
      />
      {info && <p className="error">{info}</p>}
      <Button
        style={styles.button}
        onClick={handleRegisterAdmin}
      >
        Załóż konto Drużynowego
      </Button>
      <TouchableOpacity>
        <Link to="/login">
            <Text style={styles.link}>Masz już konto? Zaloguj się</Text>
        </Link>
      </TouchableOpacity>
      <br></br>
    </View>
  );
};

export default RegisterAdmin;
