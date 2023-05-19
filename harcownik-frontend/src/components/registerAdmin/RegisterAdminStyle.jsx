import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
    container: {
      flex: 1,
      alignItems: "center",
      justifyContent: "center",
    },
    title: {
      fontSize: 24,
      fontWeight: "bold",
      marginBottom: 20,
    },
    input: {
      width: "40%",
      height: 50,
      borderWidth: 1,
      borderColor: "#ccc",
      borderRadius: 5,
      paddingHorizontal: 10,
      marginBottom: 20,
    },
    button: {
      width: "40%", 
      height: 50,
      backgroundColor: "#007bff",
      borderRadius: 5,
      alignItems: "center",
      justifyContent: "center",
      marginBottom: 20,
    },
    link: {
      color: "#007bff",
    },
  });

export default styles;