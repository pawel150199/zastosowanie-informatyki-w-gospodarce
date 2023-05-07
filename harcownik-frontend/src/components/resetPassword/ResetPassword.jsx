import React, { useState } from "react";
import { View, Text, TextInput, TouchableOpacity } from "react-native";

import axios from "../../api/api";
import { getLoginStatus, getLocalToken } from "../../api/utils";

import styles from "./ResetPasswordStyle";

const ResetPassword = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [newRepeatedPassword, setNewRepeatedPassword] = useState("");

  const handleResetPassword = async () => {
    if (getLoginStatus("isLogged")) {
        if (newPassword ===  newRepeatedPassword) {
            axios.post("/reset-password", {
                token: getLocalToken("token"),
                new_password: newPassword
            })
                .then(() => {
                    console.log("Password succesfully changed");
                    window.location.href = "/user";
                })
                .catch((error) => {
                    console.error("Error: ",  error);
                });
        }
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Reset Hasła</Text>
      <TextInput
        style={styles.input}
        placeholder="Email"
        value={username}
        onChangeText={setUsername}
      />
      <TextInput
        style={styles.input}
        placeholder="Stare hasło"
        secureTextEntry={true}
        value={password}
        onChangeText={setPassword}
      />
      <TextInput
        style={styles.input}
        placeholder="Nowe hasło"
        secureTextEntry={true}
        value={newPassword}
        onChangeText={setNewPassword}
      />
      <TextInput
        style={styles.input}
        placeholder="Powtórz nowe hasło"
        secureTextEntry={true}
        value={newRepeatedPassword}
        onChangeText={setNewRepeatedPassword}
      />
      <TouchableOpacity
        style={styles.button}
        onPress={handleResetPassword}
      >
        <Text>Zmień hasło</Text>
      </TouchableOpacity>
    </View>
  );
};

export default ResetPassword;
