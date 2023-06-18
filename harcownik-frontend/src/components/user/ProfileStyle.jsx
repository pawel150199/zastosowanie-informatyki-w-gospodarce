import { StyleSheet } from "react-native";

const styles = StyleSheet.create({
  cardcontainer: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
    height: "30rem",
  },
  skillsContainer: {
    flex: 1,
    alignItems: "left",
    justifyContent: "center",
    padding: 20,
    height: "30rem",
  },
  imageContainer: {
    width: "10rem",
    height: "10rem",
    borderRadius: 75,
    overflow: "hidden",
    marginBottom: 10,
  },
  image: {
    width: "100%",
    height: "100%",
    resizeMode: "cover",
  },
  textContainer: {
    alignItems: "center",
  },
  textInformation: {
    alignItems: "center",
  },
  divider: {
    borderBottomWidth: 1,
    borderBottomColor: "black",
    marginVertical: 10,
  },
  badgeContainer: {
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    marginBottom: 4,
  },
  customBadge: {
    backgroundColor: "gray",
  },
  badgeText: {
    color: "white",
    fontSize: 22,
  },
  heading: {
    fontSize: 40,
    marginBottom: 10,
    textAlign: "center",
  },
});

export default styles;
