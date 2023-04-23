import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity } from "react-native";
import { Button } from "react-bootstrap";
import { Link } from "react-router-dom";

import styles from "./RegisterStyle";

const Register = () => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");

  const handleRegister = () => {
    // perform registration authentication
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Register</Text>
      <TextInput
        style={styles.input}
        placeholder="Email"
        keyboardType="email-address"
        value={email}
        onChangeText={setEmail}
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry={true}
        value={password}
        onChangeText={setPassword}
      />
      <TextInput
        style={styles.input}
        placeholder="Confirm Password"
        secureTextEntry={true}
        value={confirmPassword}
        onChangeText={setConfirmPassword}
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
