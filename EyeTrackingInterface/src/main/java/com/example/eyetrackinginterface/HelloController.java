package com.example.eyetrackinginterface;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.stage.Stage;

import java.io.IOException;

public class HelloController {

    @FXML
    private Button closeButton;

    @FXML
    private Label mainLabel;


    ////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // CLAVIER

    @FXML
    public void closeButtonOnAction(ActionEvent e){
        Stage stage = (Stage) closeButton.getScene().getWindow();
        stage.close();
    }

    String oldText;

    @FXML
    public void firstAButtonOnAction(ActionEvent e) throws IOException {
//        oldText =  mainLabel.getText();
//        mainLabel.setText(oldText + "A");

        Stage current_stage = (Stage) closeButton.getScene().getWindow();

        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("first-button-view.fxml"));
        Parent root = (Parent) fxmlLoader.load();

        AController controller = fxmlLoader.getController();
        controller.setOldText(mainLabel.getText());

        current_stage.setScene(new Scene(root));

    }
    @FXML
    public void firstBButtonOnAction(ActionEvent e){
        oldText =  mainLabel.getText();
        mainLabel.setText(oldText + "B");    }
    @FXML
    public void firstCButtonOnAction(ActionEvent e){
        oldText =  mainLabel.getText();
        mainLabel.setText(oldText + "C");}

    @FXML
    public void deleteButtonOnAction(ActionEvent e) {
        oldText = mainLabel.getText();

        if (!oldText.isEmpty()) {
            String newText = oldText.substring(0, oldText.length() - 1);
            mainLabel.setText(newText);
        }
    }
    @FXML
    public void spaceButtonOnAction(ActionEvent e){
        oldText =  mainLabel.getText();
        mainLabel.setText(oldText + " ");
    }

    public void setOldText(String oldtext) throws IOException {
        if (oldtext != null) {
            mainLabel.setText(oldtext);
        }
    }

    ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    // MENU

    @FXML
    public void clavierButtonOnAction(ActionEvent e) throws IOException {

        Stage current_stage = (Stage) closeButton.getScene().getWindow();

        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("hello-view.fxml"));
        Parent root = (Parent) fxmlLoader.load();

        current_stage.setScene(new Scene(root));

    }

    @FXML
    public void menuButtonOnAction(ActionEvent e) throws IOException {

        Stage current_stage = (Stage) closeButton.getScene().getWindow();

        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("menu-view.fxml"));
        Parent root = (Parent) fxmlLoader.load();

        current_stage.setScene(new Scene(root));

    }




}