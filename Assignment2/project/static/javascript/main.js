const emailREGX =
  /^[a-zA-Z0-9.a-zA-Z0-9.!#$%&'*+-/=?^_`{|}~]+@[a-zA-Z0-9]+\.[a-zA-Z]+/;
const phoneREGX = /(^[0-9]{10}$)/;
const nameREGX = /(^[a-zA-Z ]{8,}$)/;

/**
 * Validates user input before post to server.
 */
const validate = () => {
  const nameInput = document.querySelector("#name");
  const emailInput = document.querySelector("#email");
  const phoneInput = document.querySelector("#phone");
  try {
    if (!nameREGX.test(nameInput.value)) {
      throw "Invalid full name minimum 8 characters long";
    }
    if (!emailREGX.test(emailInput.value)) {
      throw "Invalid email example@example.com";
    }
    if (!phoneREGX.test(phoneInput.value)) {
      throw "Invalid phone must be 10 digits long";
    }
  } catch (error) {
    alert(error);
    return false;
  }
  return true;
};
