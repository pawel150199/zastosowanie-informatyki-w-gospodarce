import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity } from "react-native";

import axios from "../../api/api";
import { loginHeader } from "../../api/authHeader";
import { saveLocalToken } from "../../api/utils";

import styles from "./LoginStyle";

const Login = () => {
  const [isLogged, setIsLogged] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    const headers = loginHeader();

    try {
      const response = await axios.post("/login/access-token", {
        username: username,
        password: password
      }, { headers });
      console.log(response.data.access_token)
      const accessToken = response.data.access_token;
      saveLocalToken(accessToken);
      
      window.location.href = "/user";
    } catch (error) {
      console.error("Error!" + error);
    }
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Login</Text>
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
      <TouchableOpacity
        style={styles.button}
        onPress={handleLogin}
      >
        <Text>Login</Text>
      </TouchableOpacity>
      <TouchableOpacity>
        <Text style={styles.link}>Forgot Password?</Text>
      </TouchableOpacity>
    </View>
  );
};

export default Login;
