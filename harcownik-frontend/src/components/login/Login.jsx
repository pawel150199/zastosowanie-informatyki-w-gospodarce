import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity } from "react-native";

import axios from "../../api/api";
import { loginHeader } from "../../api/authHeader";
import { saveLocalToken } from "../../api/utils";

import styles from "./LoginStyle";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [info, setInfo] = useState(" ");

  const clearInputs = () => {
    setUsername("");
    setPassword("");
  }

  const handleLogin = async () => {
    const headers = loginHeader();
    try {
      const response = await axios.post("/login/access-token", {
        username: username,
        password: password
      }, { headers });
      const accessToken = response.data.access_token;
      saveLocalToken(accessToken);
      window.location.href = "/user";
    } catch (error) {
      console.error("Error!", error);
      clearInputs();
      setInfo("Niepoprawne dane! Sprawdz dane i spóbuj ponownie.");
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Zaloguj się</Text>
      <TextInput
        style={styles.input}
        placeholder="Username"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        style={styles.input}
        placeholder="Password"
        secureTextEntry={true}
        value={password}
        onChangeText={setPassword}
      />
      {info && <p className="error">{info}</p>}
      <TouchableOpacity
        style={styles.button}
        onPress={handleLogin}
      >
        <Text>Login</Text>
      </TouchableOpacity>
      <TouchableOpacity>
        <Text style={styles.link}>Zapomniałeś/aś hasła?</Text>
      </TouchableOpacity>
    </View>
  );
};

export default Login;
