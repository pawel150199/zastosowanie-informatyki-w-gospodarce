/* eslint-disable */
import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity, Picker } from "react-native";
import { Button } from "react-bootstrap";
import { Link } from "react-router-dom";

import axios from "../../api/api"
import authHeader from "../../api/authHeader";
import addAdmin from "./addAdmin";
import addGroup from "./addGroup";
import scoutLevels from "../scoutData/scoutLevels";
import scoutFunctions from "../scoutData/scoutFunctions";

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
  const [info, setInfo] = useState("");

  const handleRegisterAdmin = async () => {
    try {
      const group = await addGroup(name, number, szczep, city);
      const admin = await addAdmin(firstName, lastName, email, level, func, password, confirmPassword, group.data.id);
      setInfo("Drużynowy i grupa stworzono pomyślnie!");
      window.location.href = "/login";
    } catch (error) {
      setInfo("Wystąpił błąd: " + error.message);
      console.error(error);
    }
  };

  return (
    <View style={styles.container}>
      <br></br>
      <Text style={styles.title}>Załóż nową drużynę Harcerską</Text>
      <small>Jeśli twoja drużyna jest już w aplikacji harcownik, poproś swojego drużynowego o dodanie :)</small>
      <br></br>
      <TextInput
        style={styles.input}
        placeholder="Nazwa Drużyny"
        value={name}
        onChangeText={setName}
      />
      <TextInput
        style={styles.input}
        placeholder="Numer Szczepu"
        value={number}
        onChangeText={setNumber}
      />
      <TextInput
        style={styles.input}
        placeholder="Nazwa Szczepu"
        value={szczep}
        onChangeText={setSzczep}
      />
      <TextInput
        style={styles.input}
        placeholder="Miasto"
        value={city}
        onChangeText={setCity}
      />

      <br></br>
      <Text style={styles.title}>Załóż konto Drużynowego</Text>
      <small>Konto Drużynowego zostanie automatycznie dodane do drużyny</small>
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
      <Picker
        style={styles.input}
        selectedValue={level}
        onValueChange={setLevel}
      >
        <Picker.Item label="Wybierz stopień" value="Wartość domyślna" />
        {scoutLevels.map((scoutLevel, index) => (
          <Picker.Item key={index} label={scoutLevel} value={scoutLevel} />
        ))}
      </Picker>
      <Picker
        style={styles.input}
        selectedValue={func}
        onValueChange={setFunc}
      >
        <Picker.Item label="Wybierz pełnioną funkcje" value="WWartość domyślna" />
        {scoutFunctions.map((scoutFunctions, index) => (
          <Picker.Item key={index} label={scoutFunctions} value={scoutFunctions} />
        ))}
      </Picker>
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
