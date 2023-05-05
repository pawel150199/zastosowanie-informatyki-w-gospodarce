import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity } from "react-native";
import { Button } from "react-bootstrap";
import { Link } from "react-router-dom";

import styles from "./RegisterStyle";

const Register = () => {
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [level, setLevel] = useState("");
  const [func, setFunc] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [group, setGroup] = useState("");
  const [badges, setBadges] = useState("");

  const handleRegister = () => {
    // perform registration authentication
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Register</Text>
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
        onChangeText={setFirstName}
      />
      <TextInput
        style={styles.input}
        placeholder="Poziom harcerza"
        value={level}
        onChangeText={setLevel}
      />
      <TextInput
        style={styles.input}
        placeholder="Pełniona funkcja w harcerstwie"
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
      <TextInput
        style={styles.input}
        placeholder="Drużyna do której należy harcerz"
        value={group}
        onChangeText={setGroup}
      />
      <Button
        style={styles.button}
        onPress={handleRegister}
      >
        Register
      </Button>
      <TouchableOpacity>
        <Link to="/login">
            <Text style={styles.link}>Already have an account? Login</Text>
        </Link>
      </TouchableOpacity>
    </View>
  );
};

export default Register;
