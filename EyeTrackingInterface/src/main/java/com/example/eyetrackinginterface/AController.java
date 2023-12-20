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

public class AController {

    @FXML
    private Button closeButton;

    @FXML
    private Button backButton;

    @FXML
    private Label mainLabel;

    String oldText;

    @FXML
    public void closeButtonOnAction(ActionEvent e){
        Stage stage = (Stage) closeButton.getScene().getWindow();
        stage.close();
    }

    @FXML
    public void secondAButtonOnAction(ActionEvent e) throws IOException {
        oldText =  mainLabel.getText();
        mainLabel.setText(oldText + "A");
    }
    @FXML
    public void firstDButtonOnAction(ActionEvent e){
        oldText =  mainLabel.getText();
        mainLabel.setText(oldText + "D");    }
    @FXML
    public void firstEButtonOnAction(ActionEvent e){
        oldText =  mainLabel.getText();
        mainLabel.setText(oldText + "E");    }
    @FXML
    public void firstFButtonOnAction(ActionEvent e){
        oldText =  mainLabel.getText();
        mainLabel.setText(oldText + "F");}


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

    @FXML
    public void backButtonOnAction(ActionEvent e) throws IOException {

        Stage current_stage = (Stage) closeButton.getScene().getWindow();

        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("hello-view.fxml"));
        Parent root = (Parent) fxmlLoader.load();

        HelloController controller = fxmlLoader.getController();
        controller.setOldText(mainLabel.getText());

        current_stage.setScene(new Scene(root));
    }

    public void setOldText(String oldtext) throws IOException {
        if (oldtext != null) {
            mainLabel.setText(oldtext);
        }
    }

}