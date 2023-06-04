/* eslint-disable */
import React, { useState } from "react";
import { View, Text, TextInput, Picker} from "react-native";
import { Button } from "react-bootstrap";

import axios from "../../api/api";
import authHeader from "../../api/authHeader";
import scoutFunctions from "../scoutData/scoutFunctions";
import scoutLevels from "../scoutData/scoutLevels";

import styles from "./RegisterScoutStyle";

const Register = () => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [level, setLevel] = useState("");
  const [func, setFunc] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [info, setInfo] = useState("");

  const handleRegister = async () => {
    const clearInputs = () => {
      setFirstName("");
      setLastName("");
      setLevel("");
      setFunc("");
      setEmail("");
      setPassword("");
      setConfirmPassword("");
    }
    try {
      if (password === confirmPassword) {
        const response = await axios.post(
          "/users/scout/",
          {
            first_name: firstName,
            last_name: lastName,
            email: email,
            level: level,
            function: func,
            password: password,
          },
          authHeader()
        );
        clearInputs();
        setInfo("Harcerz został poprawnie dodany");
      }
    } catch (error) {
      console.error(error);
      setInfo("Harcerz nie został poprawnie dodany! Spróbuj ponownie");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Dodawanie nowego harcerza do drużyny</Text>
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
        {scoutLevels.map((scoutLevel, index) => (
          <Picker.Item key={index} label={scoutLevel} value={scoutLevel} />
        ))}
      </Picker>
      <Picker
        style={styles.input}
        selectedValue={func}
        onValueChange={setFunc}
      >
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
      <Button style={styles.button} onClick={handleRegister}>
        Dodaj Harcerza
      </Button>
    </View>
  );
};

export default Register;
