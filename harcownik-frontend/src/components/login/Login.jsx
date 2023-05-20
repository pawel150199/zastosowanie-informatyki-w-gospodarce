import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity } from "react-native";

import axios from "../../api/api";
import { loginHeader } from "../../api/authHeader";
import { saveLocalToken } from "../../api/utils";
import isLogged from "../../api/isLogged";

import styles from "./LoginStyle";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    const headers = loginHeader();
    try {
      const response = await axios.post("/login/access-token", {
        username: username,
        password: password
      }, { headers });
      console.log(response.data.access_token);
      const accessToken = response.data.access_token;
      saveLocalToken(accessToken);

      console.log("You are Logged: ", isLogged());
      
      window.location.href = "/user";
    } catch (error) {
      console.error("Error!", error);
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
