* {box-sizing: border-box;}

/* Style the navbar */
.topnav {
  overflow: hidden;
  background-color: #e9e9e9;
}

/* Navbar links */
.topnav a {
  float: left;
  display: block;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

/* Navbar links on mouse-over */
.topnav a:hover {
  background-color: #ddd;
  color: black;
}

/* Active/current link */
.topnav a.active {
  background-color: #2196F3;
  color: white;
}

/* Style the input container */
.topnav .search-container {
  float: right;
}

/* Style the input field inside the navbar */
.topnav input[type=text] {
  padding: 6px;
  margin-top: 8px;
  font-size: 17px;
  border: none;
}

/* Style the button inside the input container */
.topnav .search-container button {
  float: right;
  padding: 6px;
  margin-top: 8px;
  margin-right: 16px;
  background: #ddd;
  font-size: 17px;
  border: none;
  cursor: pointer;
}

.topnav .search-container button:hover {
  background: #ccc;
}

/* Add responsiveness - On small screens, display the navbar vertically instead of horizontally */
@media screen and (max-width: 600px) {
  .topnav .search-container {
    float: none;
  }
  .topnav a, .topnav input[type=text], .topnav .search-container button {
    float: none;
    display: block;
    text-align: left;
    width: 100%;
    margin: 0;
    padding: 14px;
  }
  .topnav input[type=text] {
    border: 1px solid #ccc;
  }
}