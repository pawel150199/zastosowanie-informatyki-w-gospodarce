import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity } from "react-native";
import { Button } from "react-bootstrap";
import { Link } from "react-router-dom";

import styles from "./RegisterScoutStyle";

const Register = () => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [level, setLevel] = useState("");
  const [func, setFunc] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handleRegister = async () => {
    try {
      console.log(password, confirmPassword)
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
        if (response.status === 200  || response.status === 201) {
          setInfo("Harcerz został poprrawnie dodany");
        } else{
          setInfo("Harcerz nie został poprawnie dodany");
        }
      }
    } catch (error) {
      console.error(error);
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
      <TextInput
        style={styles.input}
        placeholder="Poziom harcerza"
        value={level}
        onChangeText={setLevel}
      />
      <TextInput
        style={styles.input}
        placeholder="Funkcja harcerza"
        value={level}
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
      <TextInput
        style={styles.input}
        placeholder="Drużyna do której należy Druży"
        value={group}
        onChangeText={setGroup}
      />
      <Button
        style={styles.button}
        onPress={handleRegister}
      >
        Załóż konto
      </Button>
      <TouchableOpacity>
        <Link to="/login">
            <Text style={styles.link}>Masz już konto? Zaloguj się</Text>
        </Link>
      </TouchableOpacity>
    </View>
  );
};

export default Register;
